# Infinity-Lang
Infinity Programming Language. A simple weakly-typed, and interpreted language.

---

Code Samples comapred to C++:

---

### Variable declaration:

#### Infinity
```rust
let a = 5;
let b = false;
let c = "hello";
```

#### C++
```cpp
#include <string>

int a = 5;
bool b = false;
std::string c = "hello";
```

---

### If statement:

#### Infinity
```rust
let a = 5;

if a == 5 then do_some_work() elif a == 6 then do_other_work() else do_work();

if a == 5 then
    do_some_work();
elif a == 6 then
    do_other_work();
else
    do_work();
end;
```

#### C++
```cpp
int a = 5;

if (a == 5)
{
    do_some_work();
}
else if (a == (5 + 1))
{
    do_other_work();
}
else
{
    do_work();
}
```

---

### For loop:

#### Infinity
```rust
for i = 0 to 10 inc 1 then
    std::println("working...");
end;
```

#### C++
```cpp
for (int i = 0; i < 10; i++)
{
    std::cout << "working...\n";
}
```

---

### While loop:

#### Infinity
```rust
let a = 5;
while a == 5 then do_work();

while a == 5 then
    do_work();
end;
```

#### C++
```cpp
int a = 5;
while (a == 5)
{
    do_work();
}
```

---

### Function declaration:

#### Infinity
```rust
fn foo(a) -> a;

fn foo(a)
    return a;
end;
```

#### C++
```cpp
int foo(int a)
{
    return a;
}
```

---

### Dynamic container:

#### Infinity
```rust
fn print_container()
    let container = std::list::new([1, 2, 3, 4]);

    std::list::push_back(container, 5);

    for i = 0 to std::list::len(container) then
        let index = std::to_string(i);
        let value = std::to_string(container/i);

        std::println("Element at index: " + index + " = " + value);
    end;
end;
```

#### C++
```cpp
#include <iostream>
#include <vector>

void print_container()
{
    std::vector<int> container = std::vector<int>(1, 2, 3, 4);

    container.emplace_back(5);

    for (size_t i = 0; i < container.size(); i++)
    {
        std::cout << "Element at index: " << i << " = " << container[i] << '\n';
    }
}
```