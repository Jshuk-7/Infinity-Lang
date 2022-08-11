# Infinity-Lang
Infinity Programming Language. A simple weakly-typed, interpreted programming language.

Code Samples comapred to C++:

### Variable declaration:

#### Infinity
```rust
let a = 5
let b = false
let c = "hello"
```

#### C++
```cpp
int a = 5;
bool b = false;
std::string c = "hello";
```

### If statement:

#### Infinity
```rust
let a = 5

if a == 5 then do_some_work() elif a == 6 then do_other_work() else do_work()

if a == 5 then
	do_some_work()
end
elif a == 6 then
	do_other_work()
end
else do_work()
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

### For loop:

#### Infinity
```rust
for i = 0 to 10 inc 1 then
	std::println("hello")
end
```

#### C++
```cpp
for (int i = 0; i < 10; i++)
{
	std::cout << "hello\n";
}
```

### While loop:

#### Infinity
```rust
let a = 5
while a == 5 then do_work()

while a == 5 then
	do_work()
end
```

#### C++
```cpp
int a = 5;
while (a == 5)
{
	do_work();
}
```

### Function declaration:

#### Infinity
```rust
fn foo(a) -> a

fn foo(a)
	return a
end
```

#### C++
```cpp
int foo(int a)
{
	return a;
}
```