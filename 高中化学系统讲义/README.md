# 高中化学系统讲义（LaTeX 源文件与 PDF）

以本仓库 `选必1/` 的七份课件（1.1 反应热 ～ 2.4 化学反应的调控六讲，以及收录 2025 年广东卷原理题的“演示文稿1”）为主线，参考配套课后作业、`思维导图/`、`高考一轮知识清单/`，并整合 `校本课/` 中的广东高考真题（2024/2025/2026），补齐高一必备基础与高三综合内容，编写而成的一本完整讲义。面向广东新高考，目标 90 分。

## 文件

| 文件 | 说明 |
| --- | --- |
| `高中化学系统讲义.pdf` | 成书 PDF，可直接阅读、打印（A4，127 页） |
| `高中化学系统讲义.tex` | 单文件完整源码（由下面的分文件合并而成，内容相同），可单独编译 |
| `main.tex` | 分文件版主文件 |
| `preamble.tex` | 版式、字体、栏目环境与常用宏 |
| `chapters/*.tex` | 各章源码（`front` 封面·前言·命题分析，`ch00`～`ch14`，`appendix` 附录） |

## 全书结构

| 篇 | 章 |
| --- | --- |
| 前置 | 前言；广东卷命题分析（试卷结构、2024–2026 逐题考点、高频考点与趋势、冲刺 90 分策略） |
| 预备篇 | 第 0 章 高一必备基础速览 |
| 原理篇（课件主线） | 第 1 章 热效应；第 2 章 速率与历程；第 3 章 化学平衡；第 4 章 水溶液中的离子平衡；第 5 章 化学反应与电能 |
| 结构篇 | 第 6 章 原子结构；第 7 章 分子结构；第 8 章 晶体结构 |
| 有机篇 | 第 9 章 结构与烃；第 10 章 烃的衍生物；第 11 章 大分子与合成 |
| 综合篇 | 第 12 章 化学实验综合；第 13 章 元素化合物与化工流程；第 14 章 高考综合大题训练 |
| 附录 | A 课件勘误汇总；B 常用数据；C 答题规范用语 |

正文穿插核心概念、追本溯源、例题、真题链接、课件勘误和视野拓展等栏目。章末有知识总结、方法提升、易错点归纳和分层练习（A 基础巩固 / B 高考典型 / C 冲击高分），练习的完整解析统一放在练习之后。

## 真题来源说明

- 引用的真题均来自本仓库 `校本课/` 中的广东卷 2024、2025、2026（网络收集版），在书中注明“年份·地区·题号”；改编题标“改编”，其余为“原创”。
- 编写时云端环境的网络策略拦截了教育部、教育考试院等站点，未能联网核对官方原卷；若与官方版本有出入，以官方发布为准。

## 编译

需要 TeX Live 2023 或更新版本（XeLaTeX；本书在 TeX Live 2023 下编译通过），以及以下字体：

- 西文：TeX Gyre Termes / Heros / Termes Math（TeX Live 自带）
- 中文：Noto Serif CJK SC、Noto Sans CJK SC、AR PL KaitiM GB（楷体）

```bash
xelatex 高中化学系统讲义.tex
xelatex 高中化学系统讲义.tex   # 第二遍生成目录与交叉引用
```

分文件版同理：`xelatex main.tex` 两遍。全书含大量 `mhchem` 化学式，单遍编译约需 4～5 分钟。

在 Windows 上若没有上述中文字体，可把 `preamble.tex`（或单文件版开头）中的字体名换成系统字体，例如：

```latex
\setCJKmainfont{SimSun}[BoldFont={SimHei},ItalicFont={KaiTi}]
\setCJKsansfont{SimHei}
\setCJKmonofont{SimHei}
\setCJKfamilyfont{zhsong}{SimSun}
\setCJKfamilyfont{zhhei}{SimHei}
\setCJKfamilyfont{zhkai}{KaiTi}
\setCJKfamilyfont{zhfs}{FangSong}
```

用到的主要宏包：`ctex`、`mhchem`、`chemfig`、`tikz`、`pgfplots`、`tcolorbox`、`tasks`、`enumitem`、`booktabs`、`tabularx`、`siunitx`、`unicode-math`。
