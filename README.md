# Zettelkasten

This is my personal [zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) based on the work of [Niklas Luhmann](https://en.wikipedia.org/wiki/Niklas_Luhmann). It all started after reading Edwin Wenink's post [building a note-taking system with vanilla vim](https://www.edwinwenink.xyz/posts/42-vim_notetaking/). At the end, he mentions that the folder structure became too complicated and instead he plans to allow for organic growth zettelkasten style. I thought, "Wow, zettelkasten sounds German. My last name sounds German. I should look this up!". I find it crazy what motivates us. ~~Hours~~ Days later after going down the multiple ~~layers of hell~~ rabbit holes, I settled using [vimwiki](https://github.com/vimwiki) with the [vim-zettel](https://github.com/michal-h21/vim-zettel) plugin. I am using [Zotero](https://www.zotero.org) as my reference manager. This set up is nice because with only a little bit of extra work it is fully compatible with [Zettlr](https://www.zettlr.com). Now, I have the option of a nice GUI, or I can stick to the command line, and vim, and feel like a badass.

## Inspiration

The following sources have been influential in the creation and structure of my zettelkasten.
- [Zettelkasten.de](https://zettelkasten.de)
- [How to Take Smart Notes](https://takesmartnotes.com)
- [r/Zettelkasten](https://www.reddit.com/r/Zettelkasten/)
- [The Zettelkasten Manifesto](https://www.youtube.com/watch?v=c5Tst3-zcWI)
- [Understanding ZettelKasten](https://medium.com/@ethomasv/understanding-zettelkasten-d0ca5bb1f80e)
- [zk.zettel.page](https://zk.zettel.page)


## Configuration

I use markdown instead of the wiki syntax (partly because I am lazy and down want to learn wiki, but mostly to make it more compatible with other resources I use). I added the `.md` when vimwiki creates a new file and changed the format of the file name to `yyyymmddHHMM.md`. This allows links to be clickable and files names to match when using Zettlr. In addition to vimwiki tags (e.g. :tag:) I also add hashtags (e.g. #tag). This allows me to search tags directly in vim and use the tag feature in Zettlr. I added a function to my ~/.vimrc that adds hashtags. It is mapped to `<leader>at`.

In addition to vimwiki and vim-zettel I have added a couple more Vim Plugins to make the writing experience more enjoyable: [pencil](https://github.com/reedes/vim-pencil), [goyo](https:/github.com/junegunn/goyo.vim). After using this setup for a couple of weeks, I have come to realize that Pencil is amazing <3. I am not yet sold on Goyo. I like it and all, but I typical forget to turn it on.

The relevant portions of my ~/.vimrc are found below.

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
"Look, I know the command in ZettleNew, but in my brain mapping it to `<leader>NewZettel` makes so much more sense
nnoremap <leader>nz :ZettelNew<space>

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

"=====[ Add Tags Function ]===================

function! AddTags()
    normal! mm0wly$$p`mlv$:s/\%V:/ #/g
Akbkbýa
endfunction
nnoremap <leader>at :call AddTags()<cr>

```
