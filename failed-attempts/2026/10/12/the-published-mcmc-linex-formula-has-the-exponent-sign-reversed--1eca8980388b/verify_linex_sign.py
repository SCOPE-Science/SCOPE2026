import math


def correct_linex(draws,h):
    return -(1.0/h)*math.log(sum(math.exp(-h*x) for x in draws)/len(draws))


def printed_linex(draws,h):
    return -(1.0/h)*math.log(sum(math.exp(+h*x) for x in draws)/len(draws))

for draws in ([1.0,1.2,1.4],[0.2,0.5,0.9,1.1],[2.0,2.5,3.0]):
    for h in (0.25,0.5,1.0):
        c=correct_linex(draws,h)
        p=printed_linex(draws,h)
        assert c>0
        assert p<0
        # Direct sample analogue of E exp(-h g).
        rhs=-(1.0/h)*math.log(sum(math.exp(-h*x) for x in draws)/len(draws))
        assert abs(c-rhs)<1e-15

truth=1.3
# Any literal printed estimate is negative under h>0 and positive draws.
for p in (-1e-12,-0.1,-1.0,-5.0):
    assert (p-truth)**2 > truth**2
assert abs(truth**2-1.69) < 1e-12
reported_mse=0.0032
assert reported_mse < truth**2

example=[1.15,1.25,1.30,1.35,1.45]
h=0.5
c=correct_linex(example,h)
p=printed_linex(example,h)
print('VERIFY_OK')
print('correct_example',format(c,'.15f'))
print('printed_example',format(p,'.15f'))
print('mse_lower_bound',format(truth**2,'.12f'))
print('reported_mse',format(reported_mse,'.12f'))
