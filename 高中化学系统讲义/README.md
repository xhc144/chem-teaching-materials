# 高中化学系统讲义

面向学完高一、尚未学习高二化学的学生，覆盖三册选择性必修、必要前置知识、实验、化工流程与综合训练。全书196页，A4单栏，包含目录、章末练习与完整解析。

## 文件

- [高中化学系统讲义.pdf](高中化学系统讲义.pdf)：完整讲义，已实际编译并检查。
- [高中化学系统讲义.tex](高中化学系统讲义.tex)：可独立编译的单文件完整源码；全部图示由TikZ/chemfig绘制，不依赖外部图片。
- [高中化学系统讲义_源码.zip](高中化学系统讲义_源码.zip)：独立源码、分文件工程、本说明与合并脚本；解压后进入讲义目录即可按下述方法编译。
- `main.tex`、`preamble.tex`、`chapters/`：同一内容的分文件工程，便于继续维护。
- `tools/assemble_source.py`：将分文件工程合并为单文件源码。

## 编译

使用XeLaTeX，建议TeX Live 2024或更新版本。需要ctex、mhchem、chemfig、TikZ/PGFPlots、siunitx、tasks、needspace等常用组件。

字体：Noto Serif CJK SC、Noto Sans CJK SC（含粗体）、Noto Sans Mono CJK SC、AR PL KaitiM GB、TeX Gyre Termes、TeX Gyre Heros、TeX Gyre Termes Math。字体不随源码打包。

在本目录执行：

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
```

若提示目录或交叉引用变化，再运行一遍。也可用：

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
```

分文件版将上述文件名换成`main.tex`即可。修改分章源码后，可先运行`python3 tools/assemble_source.py`更新单文件源码，再编译；不要分别修改两套正文。更新源码包时需同步单文件源码、分文件工程和本说明。

课程与试题出处见书末“课程与试题资料”。
