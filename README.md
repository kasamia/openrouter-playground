# OpenRouter Playground

一个最小化的 Python 示例，用于通过 OpenRouter Chat Completions API 与模型对话。

## 环境要求

- Python 3.9+
- 一个 OpenRouter API Key

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/kasamia/openrouter-playground.git
cd openrouter-playground
```

### 2. 创建虚拟环境并安装依赖

```bash
python -m venv .venv
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

复制示例环境文件：

macOS / Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

编辑 `.env`，填入你在 OpenRouter 创建的 API Key。**不要把真实 Key 提交到 Git，也不要粘贴到公开 Issue 或聊天中。**

### 4. 运行

本示例直接从环境变量读取配置。运行前先设置环境变量：

macOS / Linux:

```bash
export OPENROUTER_API_KEY="你的新_API_Key"
python app.py "用中文介绍一下 OpenRouter"
```

Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY="你的新_API_Key"
python app.py "用中文介绍一下 OpenRouter"
```

默认模型为 `openai/gpt-4o`。如需切换模型，可设置 `OPENROUTER_MODEL` 环境变量。

## 安全提示

- 不要将 API Key 写进源代码。
- 不要提交 `.env` 文件；它已加入 `.gitignore`。
- 如果 Key 曾经意外公开，请在 OpenRouter 控制台撤销并重新生成。
