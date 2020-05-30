from deoplete.source.base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'ulf'
        self.mark = '[U]'
        self.rank = 1001
        # self.input_pattern = r'[^\w\s]$'
        self.input_pattern = r'(\.|::|->)\w*$'
        self.min_pattern_length = 1
        self.is_volatile = True

        self.vim.vars['deoplete#source#ulf#_results'] = []
        self.vim.vars['deoplete#source#ulf#_requested'] = False
        self.vim.vars['deoplete#source#ulf#_prev_input'] = ''

    def gather_candidates(self, context):
        prev_input = self.vim.vars['deoplete#source#ulf#_prev_input']
        if context['input'] == prev_input and self.vim.vars[
                'deoplete#source#ulf#_requested']:
            items = self.vim.vars['deoplete#source#ulf#_results']
            return items

        self.vim.vars['deoplete#source#ulf#_results'] = []
        self.vim.vars['deoplete#source#ulf#_requested'] = False
        self.vim.vars['deoplete#source#ulf#_prev_input'] = context['input']
        self.vim.funcs.ULF_complete({
            'target': 'deoplete#source#ulf#_results',
            'callback': 'deoplete#ulf#callback',
            'include_results': False
        })
        # self.vim.funcs.ULF_send_request('deoplete/completion')

        return []
