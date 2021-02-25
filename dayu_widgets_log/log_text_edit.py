#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2020.1
# Email : muyanru345@163.com
###################################################################
"""
MLogTextEdit
"""
import datetime

from dayu_widgets import MTextEdit, dayu_theme


class MLogTextEdit(MTextEdit):
    """
    MLogTextEdit

    It's a QTextEdit using for display progress information with different color style.
    """

    def __init__(self, parent=None):
        super(MLogTextEdit, self).__init__(parent)
        self.timestamp = False
        self.ensureCursorVisible()

    def enable_timestamp(self):
        """
        Add timestamp to start of every line.
        :return: None
        """
        self.timestamp = True

    def _get_now(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ') if self.timestamp else ''

    def _get_tab(self, num=0):
        return '&nbsp;&nbsp;&nbsp;&nbsp;' * num

    def _append_html(self, color, content, tab):
        self.append(
            u'<span style="color:{}">{}{}{}</span>'.format(color,
                                                           self._get_now(),
                                                           self._get_tab(tab),
                                                           content))

    def log(self, content, tab=0):
        """
        Append content to text edit with log color style.
        :param content: str, log context.
        :param tab: int, number of tab at start of line.
        :return: None
        """
        self._append_html(dayu_theme.secondary_text_color, content, tab)

    def info(self, content, tab=0):
        """
        Append content to text edit with info color style.
        :param content: str, info context.
        :param tab: int, number of tab at start of line.
        :return: None
        """
        self._append_html(dayu_theme.info_7, content, tab)

    def error(self, content, tab=0):
        """
        Append content to text edit with error color style.
        :param content: str, error context.
        :param tab: int, number of tab at start of line.
        :return: None
        """
        self._append_html(dayu_theme.error_7, content, tab)

    def warning(self, content, tab=0):
        """
        Append content to text edit with warning color style.
        :param content: str, warning context.
        :param tab: int, number of tab at start of line.
        :return: None
        """
        self._append_html(dayu_theme.warning_7, content, tab)

    def success(self, content, tab=0):
        """
        Append content to text edit with success color style.
        :param content: str, success context.
        :param tab: int, number of tab at start of line.
        :return: None
        """
        self._append_html(dayu_theme.success_7, content, tab)

    def divider(self, content=None):
        """
        Append a "=======" separator or "=====#content#====".
        :param content: str, divider context in the middle of separator.
        :return: None
        """
        if content:
            self.append('=' * 5 + content + '=' * 5)
        else:
            self.append('=' * 20)
