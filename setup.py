#!/usr/bin/env python3
"""
term_split パッケージのセットアップファイル
"""

from setuptools import setup

setup(
    name="term_split",
    version="1.0.0",
    description="iTerm2の画面を分割し、ブロードキャスト入力を有効化するコマンド",
    author="SIN",
    py_modules=["term_split"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "term_split=term_split:main",
        ],
    },
)
