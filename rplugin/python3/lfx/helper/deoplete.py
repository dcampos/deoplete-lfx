from lfx.helper.completion import CompletionHelper


class DeopleteCompletionHelper(CompletionHelper, method='deoplete/completion'):

    def __init__(self, lfx, vim):
        super().__init__(lfx, vim, {})

    def process_completion_items(self, items):
        super().process_completion_items(items)
        self.vim.vars['deoplete#source#lfx#_results'] = self.matches
        self.vim.vars['deoplete#source#lfx#_requested'] = True
        self.vim.vars['deoplete#source#lfx#_success'] = True
        self.vim.call('deoplete#auto_complete')
