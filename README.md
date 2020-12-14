# Zettelkasten

This is my personal zettelkasten based on the work of [Niklas Luhmann](https://en.wikipedia.org/wiki/Niklas_Luhmann). It all started after reading Edmun Wenick's post [building a note-taking system with vanilla vim](https://www.edwinwenink.xyz/posts/42-vim_notetaking/). All the way towards the end, he mentions that the folder structure soon became too compicated and instead he plans to allow for organic growth zettelkasten style. ~~Hours~~ Days later after going down the multiple ~~layers of hell~~ rabbit holes, I settled using [vimwiki](https://github.com/vimwiki) with the [vim-zettel](https://github.com/michal-h21/vim-zettel) plugin. [Zotero](https://www.zotero.org) is my reference manager. This set up is nice because with only a little bit of extra work it is fully compatible with [Zettlr](https://www.zettlr.com). Now I have the option of a nice GUI, or I can stick to the command line and vim. Finally, github acts as my backup. It also gives me access to all of my notes from my phone or a different computer if need be.  

## Inspiration

The following sources have been influential in the creation and structure of my zettelkasten.
- [Zettelkasten.de](https://zettelkasten.de)
- [How to Take Smart Notes](https://takesmartnotes.com)
- [r/Zettelkasten](https://www.reddit.com/r/Zettelkasten/)
- [The Zettelkasten Manifesto](https://www.youtube.com/watch?v=c5Tst3-zcWI)
- [Understanding ZettelKasten](https://medium.com/@ethomasv/understanding-zettelkasten-d0ca5bb1f80e)
- [zettel page](https://zk.zettel.page)


## Configuration

I use markdown sytax instead of wiki syntax (partly because I am lazy and down want to learn wiki, but mostly to make it more compatiple with other resources). I added the `.md` when vimwiki creates a new file and changed the format of the file name to yyyymmddhhmm.md. This allows links to be clickable and files names to match when using Zettlr. In addition to vimwiki :tags: I also add #tags. While it doubles the work each time I add tags, it allows me to seach tags directly in vim and use the tag feature in Zettlr.

In addition to vimwiki and vim-zettel I have added a couple more plugins to make the writing expereince more enjoyable: [pencil](https://github.com/reedes/vim-pencil), [goyo](https://github.com/junegunn/goyo.vim). 

The relevant portions of my .vimrc are found below.

```vim
"=====[ vimwiki and vim-zettel ]===================

set nocompatible
filetype plugin on
syntax on
let g:zettel_format = "%Y%m%d%H%M"
let g:vimwiki_list = [{'path': '~/path/to/zettelkasten/', 'syntax': 'markdown', 'ext': '.md'}]
let g:vimwiki_markdown_link_ext = 1
let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
let g:nv_search_paths = ['~/path/to/Zettelkasten']
let g:zettel_options = [{"front_matter" : [["tags", ""], ["citation", ""]]}]
let g:zettel_fzf_command = "rg --column --line-number --ignore-case --no-heading --color=always "
let g:vimwiki_folding = 'expr'
nnoremap <leader>zn :ZettelNew<space>

"=====[ pencil ]===================

let g:pencil#wrapModeDefault = 'soft'   " default is 'hard'
augroup pencil
  autocmd!
  autocmd FileType markdown,mkd call pencil#init()
  autocmd FileType text         call pencil#init({'wrap': 'hard'})
augroup END

"=====[ goyo ]===================

function! s:goyo_enter()
  set nonumber
  set nornu
endfunction

function! s:goyo_leave()
  set number
  set rnu
endfunction

autocmd! User GoyoEnter nested call <SID>goyo_enter()
autocmd! User GoyoLeave nested call <SID>goyo_leave()

"=====[ vim-plug ]===================

call plug#begin()
    Plug 'vimwiki/vimwiki'
    Plug 'junegunn/fzf'
    Plug 'junegunn/fzf.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'michal-h21/vim-zettel'
    Plug 'tpope/vim-fugitive'
    Plug 'reedes/vim-pencil'
call plug#end()
```
