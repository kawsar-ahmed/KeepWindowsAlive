# KeepWindowsAlive
Python script to keep windows alive by key press on idle.

Sometimes our PCs are under a domain and administrators set autolock on a specific idle iterval, say 2 minutes. It's irritating. We can use this to bypass that.

Requirements:
-------------
- Python 2.7
  - pynput 1.3


How to Run:
----------
#### Run with default options
```
python keypress_on_idle.py
```
Will check for idle time in every `30` seconds and press 'up' key if the idle time exceeds `60` seconds.

#### or 

#### Run with custom options
```
python keypress_on_idle.py 30 5 down
```
Will check for idle time in every `5` seconds and press `down` key if the idle time exceeds `30` seconds.

#### Key options
`alt`, `alt_l`, `alt_r`, `backspace`, `caps_lock`, `cmd`, `cmd_r`, `ctrl`, `ctrl_l`, `ctrl_r`, `delete`, `down`, `end`, `enter`, `esc`, `f1`, `f10`, `f11`, `f12`, `f13`, `f14`, `f15`, `f16`, `f17`, `f18`, `f19`, `f2`, `f20`, `f3`, `f4`, `f5`, `f6`, `f7`, `f8`, `f9`, `home`, `insert`, `left`, `menu`, `num_lock`, `page_down`, `page_up`, `pause`, `print_screen`, `right`, `scroll_lock`, `shift`, `shift_r`, `space`, `tab`, `up`, `A`, `B`, .... 
and all other keys
