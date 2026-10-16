# Overview
In the HybSchaDC2-project we have to handle with over-current- and short-circuit-detection. Since these two actions are in general separatable, we separate the engineering behind them in two different repositories to have a better overview of the current status of both actions.

This repository is for all engineering of the short-circuit-detection. You can find the repository for over-current-detection [here](https://github.com/EMCBDengineering/HybSchaDC2_Ueberstromerkennung).

# Version-control
The purpose is to handle all stages of the engineering version-controlled and documented. For this reason, we use Git, which is documented [here](https://git-scm.com/). Since it is open-source and documented, you can either read the Docu to understand Git or use AI for specific questions. The idea of the commits is to have an overview of what's going on. Have in mind, that other people probably had your problems too and that a solution will exist.

# Texts
You will write text and we want to use Markdown for this. Its purpose is to increase the readability of text. It's a basic .txt-file with some syntax, but can be rendered easily into a PDF. An introduction into the syntax of Markdown can be found [here](https://www.markdownguide.org/basic-syntax/). Some parts of the syntax you may know from other technical things.

## Setup via Command-Line-Interface
If you want to render it into a PDF, you can do it in the Command Line Interface via Pandoc (installtion: [here](https://pandoc.org/installing.html), CLI-example: [here](https://pandoc.org/demos.html)). Herefor, you also need MiKTeX (find it [here](https://miktex.org/download)). If you have both installed, you can run:
```
pandoc .\README.md -o .\README.pdf -V colorlinks=true
```
README.md is your file, you want to render. README.pdf is the output-name of the rendered file. -V colorlinks=true highlights all links, so that you as a user can see them visually.

## Setup via Graphical-User-Interfaces
If you don't want to work on the CLI, you can also use GUI-based Markdown-Editors. If you use them, you can also use other editors as well and switch between them. GUI-based editors allow you to export the Markdown-code directly into a PDF, with just one click. A good editor is Obsidian, which you can find [here](https://obsidian.md/). In it's basic version, it's free, but you can extend it to use it mobile and so on.