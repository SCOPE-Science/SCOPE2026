points = {"a","b","c","d","e","f","g"}
lines = {
    "abg": frozenset({"a","b","g"}), "cdg": frozenset({"c","d","g"}),
    "adf": frozenset({"a","d","f"}), "bcf": frozenset({"b","c","f"}),
    "ace": frozenset({"a","c","e"}), "bde": frozenset({"b","d","e"}),
}
params={"e","f","g"}; new=points-params; checks=0
for p in sorted(new):
    assert sum(p in L for L in lines.values()) == 3; checks += 1
for p in sorted(params):
    assert sum(p in L for L in lines.values()) == 2; checks += 1
vals=list(lines.values())
for i in range(len(vals)):
    for j in range(i+1,len(vals)):
        assert len(vals[i]&vals[j]) <= 1; checks += 1
sigma={"a":"b","b":"a","c":"d","d":"c","e":"e","f":"f","g":"g"}
line_set=set(lines.values())
for L in lines.values():
    assert frozenset(sigma[x] for x in L) in line_set; checks += 1
for p in params:
    assert sigma[p]==p; checks += 1
for p in new:
    assert sigma[p]!=p; checks += 1
assert new=={"a","b","c","d"}; checks+=1
assert params=={"e","f","g"}; checks+=1
print(f"VERIFY_OK {checks} exact finite assertions")
