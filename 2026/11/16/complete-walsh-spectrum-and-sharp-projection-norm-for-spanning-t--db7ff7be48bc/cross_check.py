#!/usr/bin/env python3
"""Pointwise independent comparison of tree enumeration and Laplacian orbit sums."""
from tree_walsh_check import DIM,N,tree,hadamard
from orbit_check import values

def main():
 direct=hadamard([int(tree(i)) for i in range(N)])
 assert direct==values, 'The two exact methods disagree at a character.'
 print('ALL_65536_FOURIER_MULTIPLIERS_AGREE_PASS')

if __name__=='__main__':main()
