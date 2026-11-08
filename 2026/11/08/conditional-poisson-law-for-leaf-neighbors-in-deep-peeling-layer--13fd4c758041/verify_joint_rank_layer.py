#!/usr/bin/env python3
"""Finite checks for the joint rank-one / peeling-layer Yule-tree law.

Run: python3 verify_joint_rank_layer.py
Requires only Python 3 standard library.

The finite checks do not certify infinite limiting results.
"""
import itertools
import math
import random
from collections import deque


def tree_stats(parents):
    n = len(parents) + 1
    adj = [[] for _ in range(n)]
    children = [[] for _ in range(n)]
    depth = [0] * n
    for i, p in enumerate(parents, 1):
        adj[i].append(p)
        adj[p].append(i)
        children[p].append(i)
        depth[i] = depth[p] + 1
    degree = [len(a) for a in adj]
    near_leaf = [any(degree[w] == 1 for w in adj[v]) for v in range(n)]
    rem_degree = degree.copy()
    layers = [-1] * n
    wave = [v for v in range(n) if rem_degree[v] <= 1]
    k = 0
    while wave:
        nxt = set()
        for v in wave:
            layers[v] = k
        for v in wave:
            for w in adj[v]:
                if layers[w] == -1:
                    rem_degree[w] -= 1
                    if rem_degree[w] <= 1:
                        nxt.add(w)
        wave = list(nxt)
        k += 1
    heights = [0] * n
    for v in range(n - 1, -1, -1):
        heights[v] = max([0] + [1 + heights[c] for c in children[v]])
    return layers, near_leaf, heights, depth, degree, children


def trapezoid(a, step):
    return (sum(a) - (a[0] + a[-1]) / 2) * step


def limiting_tails(max_k=12, end=28.0, dt=0.002):
    count = round(end / dt)
    t = [i * dt for i in range(count + 1)]
    weight = [math.exp(-x) for x in t]
    leaf_child = [1 - math.exp(-(1 - w)) for w in weight]
    survive = [1.0] * (count + 1)
    out = {}
    for h in range(1, max_k + 1):
        integral = 0.0
        nxt = [0.0] * (count + 1)
        for j in range(1, count + 1):
            integral += dt * (survive[j-1] + survive[j]) / 2
            nxt[j] = -math.expm1(-integral)
        survive = nxt
        den = trapezoid([w*s for w,s in zip(weight,survive)], dt)
        num = trapezoid([w*s*p for w,s,p in zip(weight,survive,leaf_child)], dt)
        out[h] = (den, num, num/den)
    return out



def limiting_leaf_child_pmf(max_h=12, max_j=8, end=28.0, dt=0.002):
    count = round(end / dt)
    t = [i * dt for i in range(count + 1)]
    weight = [math.exp(-x) for x in t]
    a = [1 - w for w in weight]
    surv = [1.0] * (count + 1)
    result = {}
    for h in range(1, max_h + 1):
        integral = 0.0
        nxt = [0.0] * (count + 1)
        for i in range(1, count + 1):
            integral += dt * (surv[i-1] + surv[i]) / 2
            nxt[i] = -math.expm1(-integral)
        surv = nxt
        den = trapezoid([x * y for x, y in zip(weight, surv)], dt)
        result[h] = [trapezoid([w * sh * math.exp(-v) * v**j / math.factorial(j)
                                 for w, sh, v in zip(weight, surv, a)], dt)/den
                     for j in range(max_j+1)]
    return result


def check_all():
    assertions = 0
    # The parent choices are independent, with each new vertex choosing a smaller label.
    for n in range(3, 9):
        count = 0
        for parents in itertools.product(*(range(j) for j in range(1,n))):
            layer, near, height, depth, degree, children = tree_stats(parents)
            for v in range(1,n):
                assert near[v] == (any(degree[c] == 1 for c in children[v]) or (parents[v-1] == 0 and degree[0] == 1))
                assertions += 1
                for h in (1,2,3):
                    if depth[v] > h+1:
                        assert (layer[v] >= h) == (height[v] >= h)
                        assertions += 1
            count += 1
        assert count == math.factorial(n-1)
        assertions += 1
    tails = limiting_tails()
    assert abs(tails[1][0] - 0.5) < 0.00001
    assertions += 1
    assert abs(tails[2][0] - (3-math.e)) < 0.00001
    assertions += 1
    rank1_deep2 = 2.5 + math.exp(-1) - math.e
    assert abs(tails[2][1] - rank1_deep2) < 0.00001
    assertions += 1
    assert abs(tails[2][2] - rank1_deep2/(3-math.e)) < 0.00001
    assertions += 1
    assert abs(tails[12][2] - (1-math.exp(-1))) < 0.003
    assertions += 1
    pmfs = limiting_leaf_child_pmf()
    for h in (2, 4, 8, 12):
        zero = pmfs[h][0]
        assert abs(1-zero-tails[h][2]) < 0.00001
        assertions += 1
        poisson_one = [math.exp(-1)/math.factorial(j) for j in range(9)]
        # Total variation on the full countable space is bounded by Poisson thinning.
        tv_lower = sum(abs(p-q) for p,q in zip(pmfs[h], poisson_one))/2
        analytic_bound = math.exp(-h/10) + 0.1*(math.e/5)**h
        assert tv_lower <= analytic_bound + 1.e-8
        assertions += 1
    assert sum(abs(pmfs[12][j]-math.exp(-1)/math.factorial(j)) for j in range(9))/2 < .003
    assertions += 1
    # An independent large-tree diagnostic: one draw of the recursive genealogy.
    rng = random.Random(260804303)
    n = 90000
    parents = [rng.randrange(j) for j in range(1,n)]
    layer, near, _, _, degree, children = tree_stats(parents)
    leaf_child_count = [sum(degree[c] == 1 for c in child) for child in children]
    proportions = {}
    for h in (2,3,4):
        den = sum(x >= h for x in layer) / n
        num = sum(near[i] and layer[i] >= h for i in range(n)) / n
        assert abs(den - tails[h][0]) < 0.014, (h, den, tails[h][0])
        assert abs(num - tails[h][1]) < 0.014, (h, num, tails[h][1])
        assertions += 2
        proportions[h] = (den,num)
        if h in (2,4):
            for j in (0,1,2):
                cond_prob = sum(layer[v]>=h and leaf_child_count[v]==j for v in range(n)) / (n*den)
                assert abs(cond_prob - pmfs[h][j]) < .025, (h,j,cond_prob,pmfs[h][j])
                assertions += 1
    return assertions,tails,proportions,pmfs


if __name__ == '__main__':
    k,tails,prop,pmfs = check_all()
    print('Passed assertions:', k)
    print('h   layer_tail    rank1_and_layer_tail    conditional_ratio')
    for h in (2,3,4,8,12):
        den, num, ratio = tails[h]
        print(f'{h:2d}  {den:.9f}    {num:.9f}             {ratio:.9f}')
    print('Finite n=90000 checks (layer tail, joint tail):',prop)
    print('Predicted high-layer conditional limit:',1-math.exp(-1))
    print('Conditional leaf-neighbor count, h=12, P(0), P(1), P(2):',pmfs[12][:3])
