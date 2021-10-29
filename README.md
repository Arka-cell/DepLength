DepLength is a calculator for the dependency length of sentences in English.


### What is Dependency Length?
Considering the following sentences:

![image](https://user-images.githubusercontent.com/55358999/118133805-2857bf80-b3f9-11eb-9785-effb9aad24ba.png)

Four sentences along with their dependency representations. The number over each arc represents the length of the dependency in words. The total dependency length is given below each sentence. Sentences A and B have the same semantics, and either word order is acceptable in English; English speakers typically do not find one more natural than the other. Sentences C and D also both have the same semantics, but English speakers typically find C more natural than D.

Sentence A is a sequence of  n  words, where each word is a set of other words with the uniqueness property that if  w∈x∈A  and  w∈y∈A  then  x=y . We can denote the  k<sup>th</sup>  word in  A as Ak. The sentence total dependency of a sentence  A  can be denoted:


<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{k&space;=&space;1}^{n}\sum_{w&space;\in&space;A_{k}&space;}^{}\o&space;(w)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{k&space;=&space;1}^{n}\sum_{w&space;\in&space;A_{k}&space;}^{}\o&space;(w)" title="\sum_{k = 1}^{n}\sum_{w \in A_{k} }^{}\o (w)" /></a>

where  ϕ:A↦N  satisfies  ϕ(w)=d , where  w=Aj , the unique superset of  w  is  Ak , and  |j−k|=d . More compactly, the sentence total dependency of a sentence  A  can be denoted

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{k&space;=&space;1}^{n}\sum_{w&space;=&space;A_{j}&space;\in&space;A_{k}&space;}^{}\left&space;|j&space;-&space;k&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{k&space;=&space;1}^{n}\sum_{w&space;=&space;A_{j}&space;\in&space;A_{k}&space;}^{}\left&space;|j&space;-&space;k&space;\right&space;|" title="\sum_{k = 1}^{n}\sum_{w = A_{j} \in A_{k} }^{}\left |j - k \right |" /></a>

### How to use?

```python
from depLength import depLength

sentences = """
          John threw out the trash. 
          John threw the trash out. 
          John threw out the old trash sitting in the kitchen. 
          John threw the old trash sitting in the kitchen out.
"""

res = depLength.DepLength(sentences)
print(res.sdl())
for key in res.sdl():
    print(res.getSentence(key), "has a total dependency length of:", res.sdl()[key])
```

```bash
[OUTPUT]:
{0: 6, 1: 7, 2: 14, 3: 20}
John threw out the trash. has a total dependency length of: 6
John threw the trash out. has a total dependency length of: 7
John threw out the old trash sitting in the kitchen. has a total dependency length of: 14
John threw the old trash sitting in the kitchen out. has a total dependency length of: 20
```
