# Python Exercises

### Check Prime number (num True or False)

```python
def is_Prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5)+1,2):
        if i % 2 == 0:
            return False
    
    return True
```
Example
```markdown
>>> is_Prime(5)
>>> True
```
### Count Prime number from given range 


```python
def count_Prime(a,b):
    count = 0
    for i in range(a,b+1):
        if is_Prime(i):  # Calling above number check Function 
            count +=1
    print("Prime number in the range of [{},{}]: {}".format(a,b,count))
```
example
```markdown
>>> count_Prime(3,14)
Prime number in the range of [3,14]: 6
>>> 
```
### Print Prime number from given range
```python
def Print_Prime(a,b):
    num_list = []
    for i in range(a,b+1):
        if is_Prime(i):  # calling above number check function 
            num_list.append(i)
    
    print("Prime number in the range of [{},{}]: {}".format(a,b,num_list))
```
Example
```markdown
>>> Print_Prime(3,15)
Prime number in the range of [3,15]: [3, 5, 7, 9, 11, 13, 15]
>>> 
```
### Segregate prime number from give list ([1,2,3,4,5,6,7,8])
```python
def Segregate_Prime_number(num_list):
    prime_num = []
    non_prime_num = []
    for i in num_list:
        if is_Prime(i):
            prime_num.append(i)
        else:
            non_prime_num.append(i)
    
    print("Prime Number List : {}\n Non Prime Number List : {}".format(prime_num,non_prime_num))
```
```markdown
>>> Segregate_Prime_number([1,4,2,3,2,5,1,4,6,45,12,48])
Prime Number List : [2, 3, 2, 5, 45] 
Non Prime Number List : [1, 4, 1, 4, 6, 12, 48]
>>> 
```
