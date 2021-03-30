#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2021.2
# Email : muyanru@corp.netease.com
###################################################################

from dayu_widgets_log import MLogTextEdit
from dayu_widgets.qt import *
from dayu_widgets import MDivider, dayu_theme


class MLogTextEditExample(QWidget):
    def __init__(self, parent=None):
        super(MLogTextEditExample, self).__init__(parent)
        self.log_log_text_edit = MLogTextEdit()
        self.log_log_text_edit.log('This is a log context.')
        self.log_log_text_edit.log('This is a log context with 1 tab.', 1)
        self.log_log_text_edit.log('This is a log context with 2 tabs.', 2)
        self.log_log_text_edit.log('This is a log context with 1 tab.', 1)

        self.info_log_text_edit = MLogTextEdit()
        self.info_log_text_edit.info('This is an info context.')
        self.info_log_text_edit.log('This is an info context with 2 tabs.', 2)

        self.warning_log_text_edit = MLogTextEdit()
        self.warning_log_text_edit.warning('This is a warning context.')
        self.warning_log_text_edit.warning('This is a warning context with 1 tab.', 1)

        self.error_log_text_edit = MLogTextEdit()
        self.error_log_text_edit.error('This is an error context.')
        self.error_log_text_edit.error('This is an error context with 2 tabs', 2)

        self.success_log_text_edit = MLogTextEdit()
        self.success_log_text_edit.success('This is a success context')
        self.success_log_text_edit.success('This is a success context with 1 tab', 1)

        level_lay = QHBoxLayout()
        level_lay.addWidget(self.log_log_text_edit)
        level_lay.addWidget(self.info_log_text_edit)
        level_lay.addWidget(self.warning_log_text_edit)
        level_lay.addWidget(self.error_log_text_edit)
        level_lay.addWidget(self.success_log_text_edit)

        self.enable_timestamp_text_edit = MLogTextEdit()
        self.enable_timestamp_text_edit.enable_timestamp()
        self.enable_timestamp_text_edit.log('This is a log context.')
        self.enable_timestamp_text_edit.info('This is an info context.')
        self.enable_timestamp_text_edit.warning('This is a warning context.')
        self.enable_timestamp_text_edit.error('This is an error context.')
        self.enable_timestamp_text_edit.success('This is a success context')

        self.divider_text_edit = MLogTextEdit()
        self.divider_text_edit.enable_timestamp()
        self.divider_text_edit.log('This is a log context.')
        self.divider_text_edit.log('Add a divider.')
        self.divider_text_edit.divider()
        self.divider_text_edit.info('This is an info context.')
        self.divider_text_edit.log('Add a divider with content.')
        self.divider_text_edit.divider('< start >')
        self.divider_text_edit.warning('This is a warning context.')
        self.divider_text_edit.error('This is an error context.')
        self.divider_text_edit.success('This is a success context')
        self.divider_text_edit.divider('< end >')

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Log Level'))
        main_lay.addLayout(level_lay)
        main_lay.addWidget(MDivider('Enable Timestamp'))
        main_lay.addWidget(self.enable_timestamp_text_edit)
        main_lay.addWidget(MDivider('Add Divider'))
        main_lay.addWidget(self.divider_text_edit)

        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLogTextEditExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
