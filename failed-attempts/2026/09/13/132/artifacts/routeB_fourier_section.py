#!/usr/bin/env python3
"""lane-1780 Route B: exact Fourier transfer-operator coupling + finite sections.
From k: q=Mk; modes (q1,q2-m,q3-m-l) with amplitude J_{-m}(2*pi*eps*q1)*J_{-l}(2*pi*eps*q2).
Uses mpmath.besselj at 40 digits. Result: K=2 top eig 1.0 rest~0; K=3 top 1.0,
subdominant ~4.6e-4 -- heuristic only (column-sum leakage -0.13..1.69).
"""
