# Definition:

* is highlevel, strong and dynamically typed general purpose interated language  created by Guido van Rossum used to build software, ai , ml tools...

## inteprated explained:

* python code is inteprated to bytecode. by the python intepreter.
* python virual machine (PVM) run over the code and exucutes it.

## Typing explained:

### Strongly typed:

* python is strongly typed that it does not allow arthimetic operation id d/t types like js allow

```text
eg. 5 +'5' = '55' in js
            = error in python
```

### Dynamically typed:

* python the type parsing and check is done at run time not compile time like java do.
* it allows reassigment ith d/t type because type is attached to the object not the varible and it sees every thing as object.
  when a int variable is re assigned to string python just change the pointer from int object to newly created string object and it also have is own garbage collecter to clear the mess.

```java
int x = 5;
x = '5';  // error in java but works in python
```
