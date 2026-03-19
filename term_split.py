#!/usr/bin/env python3
"""
term_split - iTerm2の画面を分割し、ブロードキャスト入力を有効化するコマンド
"""

import argparse
import os
import subprocess
import sys


def run_applescript(script: str) -> str:
    """AppleScriptを実行し、結果を返す"""
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"AppleScript error: {result.stderr}")
    return result.stdout.strip()


def get_current_directory() -> str:
    """現在のディレクトリを取得"""
    return os.getcwd()


def split_panes(count: int, vertical: bool = True) -> None:
    """iTerm2のペインを分割する"""
    direction = "vertically" if vertical else "horizontally"
    current_dir = get_current_directory()

    # 分割を実行（count-1回分割する）
    for i in range(count - 1):
        script = f'''
        tell application "iTerm2"
            tell current session of current tab of current window
                split {direction} with default profile
            end tell
        end tell
        '''
        run_applescript(script)

    # 全ペインを現在のディレクトリに移動
    script = f'''
    tell application "iTerm2"
        tell current tab of current window
            repeat with s in sessions
                tell s
                    write text "cd '{current_dir}'"
                end tell
            end repeat
        end tell
    end tell
    '''
    run_applescript(script)


def enable_broadcast() -> None:
    """ブロードキャスト入力を有効化（メニュー操作）"""
    script = '''
    tell application "iTerm2" to activate
    delay 0.3
    tell application "System Events"
        tell process "iTerm2"
            click menu item "Broadcast Input to All Panes in Current Tab" of menu 1 of menu item "Broadcast Input" of menu "Shell" of menu bar 1
        end tell
    end tell
    '''
    run_applescript(script)


def disable_broadcast() -> None:
    """ブロードキャスト入力を無効化（メニュー操作）"""
    script = '''
    tell application "iTerm2" to activate
    delay 0.3
    tell application "System Events"
        tell process "iTerm2"
            click menu item "Send Input to Current Session Only" of menu 1 of menu item "Broadcast Input" of menu "Shell" of menu bar 1
        end tell
    end tell
    '''
    run_applescript(script)


def main() -> None:
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="iTerm2の画面を分割し、ブロードキャスト入力を有効化します"
    )
    parser.add_argument(
        "count",
        type=int,
        nargs="?",
        default=None,
        help="分割数（2以上）"
    )
    parser.add_argument(
        "-H", "--horizontal",
        action="store_true",
        help="水平分割（デフォルトは垂直分割）"
    )
    parser.add_argument(
        "--off",
        action="store_true",
        help="ブロードキャスト入力を無効化"
    )

    args = parser.parse_args()

    # --off オプションの処理
    if args.off:
        try:
            print("ブロードキャストを無効化しています...")
            disable_broadcast()
            print("ブロードキャストを無効化しました。")
        except RuntimeError as e:
            print(f"エラー: {e}", file=sys.stderr)
            sys.exit(1)
        return

    # 分割数のチェック
    if args.count is None:
        parser.print_help()
        sys.exit(1)

    if args.count < 2:
        print("エラー: 分割数は2以上を指定してください", file=sys.stderr)
        sys.exit(1)

    vertical = not args.horizontal

    try:
        print(f"iTerm2を{args.count}分割しています...")
        split_panes(args.count, vertical)

        print("ブロードキャスト入力を有効化しています...")
        enable_broadcast()

        direction = "垂直" if vertical else "水平"
        print(f"\n{direction}方向に{args.count}分割しました。")
        print("ブロードキャスト入力が有効です - 入力が全てのペインに送信されます。")
        print("モード変更: Option + Cmd + I")

    except RuntimeError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"予期しないエラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
