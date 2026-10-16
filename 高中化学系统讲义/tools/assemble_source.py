#!/usr/bin/env python3
"""将分章主文件合并为可独立编译的完整 TeX。"""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
pattern = re.compile(r'\s*\\input\{([^}]+)\}\s*(?:%.*)?$')
def expand(path, stack=()):
    path = path.resolve()
    if path in stack:
        raise RuntimeError('Circular input: ' + str(path))
    output = []
    for line in path.read_text(encoding='utf-8').splitlines(keepends=True):
        match = pattern.fullmatch(line.rstrip('\n'))
        if match:
            child = root / match.group(1)
            if not child.suffix:
                child = child.with_suffix('.tex')
            output.append(expand(child, stack + (path,)))
        else:
            output.append(line)
    return ''.join(output)
source = expand(root / 'main.tex')
assert '\\input{' not in '\n'.join(line for line in source.splitlines() if not line.lstrip().startswith('%'))
# Keep the standalone source usable outside the modular project. Local template
# files are emitted by LaTeX's built-in filecontents environment when absent.
bundled = []
for dependency in sorted([*root.glob('mojing-*.cls'), *root.glob('mojing-*.sty')]):
    bundled.append('\\begin{filecontents*}{' + dependency.name + '}\n'
                   + dependency.read_text(encoding='utf-8').rstrip('\n')
                   + '\n\\end{filecontents*}\n')
source = ''.join(bundled) + source
target = root / '高中化学系统讲义.tex'
target.write_text(source, encoding='utf-8')
print(target.name, len(source), 'characters')
