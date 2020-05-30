function! deoplete#ulf#callback() abort
    let g:deoplete#source#ulf#_requested = v:true
    let g:deoplete#source#ulf#_success = v:true
    call deoplete#auto_complete()
endfunction
