from ulf.completion import CompletionHandler
from ulf.ulf import request_handler

@request_handler('deoplete/completion')
class DeopleteCompletionHandler(CompletionHandler):

    def __init__(self, ulf, vim):
        super().__init__(ulf, vim, {})

    def process_completion_items(self, items):
        super().process_completion_items(items)
        self.vim.vars['deoplete#source#ulf#_results'] = self.matches
        self.vim.vars['deoplete#source#ulf#_requested'] = True
        self.vim.vars['deoplete#source#ulf#_success'] = True
        self.vim.call('deoplete#auto_complete')
