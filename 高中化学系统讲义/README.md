# 高中化学系统讲义

面向学完高一、尚未学习高二化学的学生，覆盖三册选择性必修、必要前置知识、实验、化工流程与综合训练。全书198页，采用墨经书籍模板的A4单栏版式，包含目录、章末练习与完整解析。

## 文件

- [高中化学系统讲义.pdf](高中化学系统讲义.pdf)：完整讲义，已实际编译并检查。
- [高中化学系统讲义.tex](高中化学系统讲义.tex)：完整单文件源码，内嵌本书所用的墨经类与样式文件；在空目录中编译时会自动写出这些文件。图示由TikZ/chemfig绘制，不依赖外部图片。
- [高中化学系统讲义_源码.zip](高中化学系统讲义_源码.zip)：单文件源码、分章工程、原生模板文件、本说明与合并脚本。
- `main.tex`、`preamble.tex`、`chapters/`：分文件工程。
- `book-config.tex`：A4页面、标题留白及书名设置；化学图示的功能性配色保留在`preamble.tex`中。
- `mojing-book.cls`、`mojing-*.sty`：墨经原生书籍模板文件。
- `tools/assemble_source.py`：将分文件工程与模板文件合并为单文件源码。

## 编译

使用XeLaTeX，建议TeX Live 2025完整安装。需要latexmk、Biber，以及ctex、mhchem、chemfig、TikZ/PGFPlots、siunitx、tasks、needspace、tcolorbox、biblatex-gb7714-2015、imakeidx等组件。Biber版本应与安装的biblatex版本匹配。

模板使用Fandol宋体、黑体、楷体和仿宋，TeX Gyre Pagella及其数学字体，Source Sans Pro、Source Code Pro和STIX Two Math。注意Source Sans Pro的文件名是`SourceSansPro-*.otf`；Source Sans 3不能仅通过改名替代。字体不随源码打包。

解压源码包后进入讲义目录，执行：

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
```

latexmk会处理目录、交叉引用及biblatex初始化。也可手动运行：

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
biber 高中化学系统讲义
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error 高中化学系统讲义.tex
```

分文件版将文件名换成`main`或`main.tex`即可。修改正文、配置或模板文件后，在讲义目录运行`python3 tools/assemble_source.py`更新单文件源码，再编译PDF并同步源码包。不要分别修改两套正文。

课程与试题出处见书末“课程与试题资料”。

## 模板来源

墨经模板取自所提供的`mojing-latex.zip`；上游为[xhc144/claude-lab](https://github.com/xhc144/claude-lab/tree/35a5afc2524a4162e28a9cd9de3b9e1d32f61a0a/mojing)，版本及来源记录在`mojing-project.json`。原生类与样式文件保留原始字节及LPPL 1.3c许可声明；本书通过公开选项与`book-config.tex`设置A4讲义版式。
