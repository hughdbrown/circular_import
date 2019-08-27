```
% python s.py
{'b': 2}

% python t.py
Traceback (most recent call last):
  File "t.py", line 1, in <module>
    from s import foo as foo_s
  File "/home/hugh.brown/workspace/circular_import/circular/s.py", line 1, in <module>
    import t
  File "/home/hugh.brown/workspace/circular_import/circular/t.py", line 1, in <module>
    from s import foo as foo_s
ImportError: cannot import name foo
```
