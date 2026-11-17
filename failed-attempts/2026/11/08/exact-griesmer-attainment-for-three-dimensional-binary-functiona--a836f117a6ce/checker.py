#!/usr/bin/env python3
"""Verify all exhaustive finite recovery certificates in recovery_certificates.json.
Requires only the Python standard library. No external packages or solvers.
"""
import itertools
import json
from pathlib import Path


def binary_rank(columns):
    pivots = {}
    for c in columns:
        x=c
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x ^= pivots[p]
    return len(pivots)


def check(path):
    payload=json.loads(Path(path).read_text(encoding='utf-8'))
    assert payload['schema_version']==1
    specs=[('basis_1',[1,2,4],1,'batch'),
           ('parity_2',[1,2,4,7],2,'pir'),
           ('five_2',[1,1,2,4,6],2,'batch'),
           ('six_3',[1,2,3,4,5,6],3,'batch'),
           ('seven_4',[1,2,3,4,5,6,7],4,'batch'),
           ('eleven_6',[1,2,3,4,5,6,7,1,2,4,7],6,'batch')]
    assert len(payload['cases'])==len(specs)
    total=0
    for case,(name,columns,t,kind) in zip(payload['cases'],specs):
        assert case['name']==name and case['columns']==columns
        assert case['requests']==t and case['service']==kind
        assert binary_rank(columns)==3
        expected=(itertools.combinations_with_replacement(range(1,8),t)
                  if kind=='batch' else ((v,)*t for v in range(1,8)))
        entries=case['witnesses']
        for (request,masks),want in itertools.zip_longest(entries,expected,fillvalue=None):
            assert (request,masks) is not None and want is not None
            assert tuple(request)==tuple(want) and len(masks)==t
            used=0
            for v,mask in zip(request,masks):
                assert isinstance(mask,int) and 0<mask<(1<<len(columns))
                assert (used&mask)==0
                used|=mask
                xor=0
                for i,col in enumerate(columns):
                    if mask&(1<<i): xor ^= col
                assert xor==v
            total+=1
        print(f'{name}: {len(entries)} distinct complete request multisets verified')
    print(f'PASS: {total} exhaustive finite request instances; all recoveries independent/disjoint')


if __name__=='__main__':
    check(Path(__file__).with_name('recovery_certificates.json'))
