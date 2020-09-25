function! deoplete#lfx#callback() abort
    let g:deoplete#source#lfx#_requested = v:true
    let g:deoplete#source#lfx#_success = v:true
    call deoplete#auto_complete()
endfunction
