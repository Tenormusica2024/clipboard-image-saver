# Clipboard Image Saver

クリップボードの画像をショートカットキー（F8）で自動保存し、ファイルパスをターミナルに入力する便利ツール

## 機能

- **F8キー**: クリップボードの画像を自動保存してパスを入力
- **自動ファイル名生成**: タイムスタンプ付きファイル名（`snip_YYYYMMDD_HHMMSS.png`）
- **ログ記録**: 全操作をログファイルに記録

## インストール

### 必要なパッケージ

```bash
pip install pillow keyboard
```

### 使用方法

1. スクリプトを実行:
```bash
python snip_hotkey.py
```

2. F8キーを押す:
   - クリップボードの画像が保存される
   - ファイルパスがアクティブウィンドウに自動入力される

3. 終了: Ctrl+C

## 設定

スクリプト内の以下の変数を編集してカスタマイズ可能:

```python
SAVE_DIR = r"C:\Users\B1443kouda\Documents\Obsidian Vault\Codex\snips"
LOG_PATH = r"C:\Users\B1443kouda\Documents\Obsidian Vault\Codex\tools\snip_hotkey\snip_hotkey.log"
```

## ログ

すべての操作は `snip_hotkey.log` に記録されます:

```
[2025-12-01 10:30:45] snip_hotkey started (F8)
[2025-12-01 10:30:45] hotkey registered
[2025-12-01 10:31:20] F8 pressed
[2025-12-01 10:31:20] saved image -> C:\Users\...\snip_20251201_103120.png
[2025-12-01 10:31:20] typed path into active window
```

## 動作環境

- Windows (keyboard モジュールは Windows 専用)
- Python 3.6+
- PIL (Pillow)
- keyboard

## ライセンス

MIT License
