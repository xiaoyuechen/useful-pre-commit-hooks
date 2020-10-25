# Useful Pre-commit Hooks
A collection of useful pre-commit hooks. 

## Usage

We current support common hooks for C++ development. Here is the list: 

```cpp-hooks
cmake-format
cmake-lint
clang-format
cpplint
```

To use these hooks, simply place the following in your `.pre-commit-config.yaml`

For example: 
```yaml
repos:
  - repo: https://github.com/xiaoyuechen/useful-pre-commit-hooks.git
    rev: v0.8
    hooks: 
    - id: cmake-format
      args: [--in-place, --line-ending=auto]
    - id: cmake-lint
      args: [--disabled-codes=C0327]
    - id: clang-format
    - id: cpplint
      args: [--output=vs7]
```

Then run `pre-commit install`. Now every time when you run `git commit`, the selected 
pre-commit commands are going to run. 
