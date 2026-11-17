#!/usr/bin/env python3
"""Numerical checks of the exact inverse-beta crossing waveform and Fourier jumps.

Dependencies: Python 3, numpy, scipy. These examples verify finite samples only.
"""
import numpy as np
from scipy.special import beta, betaincinv


def clock(alpha, beta0, gamma, radius):
    k = (2 / 3) ** (2 / 3) * beta(0.5, 1 / 3) * radius ** (-1 / 3)
    positive = k * (alpha * beta0**2) ** (-1 / 3)
    negative = k * gamma ** (-1 / 3)
    return positive, negative


def position(times, alpha, beta0, gamma, radius):
    positive, negative = clock(alpha, beta0, gamma, radius)
    phase = np.mod(np.asarray(times, dtype=float), positive + negative)
    upper = phase < positive
    output = np.empty_like(phase)
    output[upper] = radius * (1 - 2 * betaincinv(1 / 3, 1 / 3, phase[upper] / positive))
    output[~upper] = radius * (-1 + 2 * betaincinv(1 / 3, 1 / 3, (phase[~upper] - positive) / negative))
    return output


def asymptotic(n, alpha, beta0, gamma, radius):
    plus, minus = clock(alpha, beta0, gamma, radius)
    period = plus + minus
    omega = 2 * np.pi / period
    theta = plus / period
    a = alpha * beta0**2
    c = gamma
    phase = np.exp(-2j * np.pi * n * theta)
    return (-2 * radius**2 * (a + c) * (1 - phase) / (period * (1j * omega * n) ** 4)
            + 20 * radius**3 * (a*a - c*c) * (1 + phase) / (period * (1j * omega * n) ** 7))


def run():
    samples = 2**17
    parameters = [(8, 1, 1, 1), (1, 1, 1, 1), (1, 2, 1, 2)]
    for params in parameters:
        plus, minus = clock(*params)
        period = plus + minus
        x = position(np.arange(samples) * period / samples, *params)
        assert np.all(np.isfinite(x))
        assert abs(x[0] - params[-1]) < 2e-12
        assert abs(x[samples // 2] + x[0]) < 2e-12 if params[0] * params[1]**2 == params[2] else True
        modes = np.fft.fft(x) / samples
        if params[0] * params[1]**2 == params[2]:
            assert np.max(np.abs(x[:samples//2] + x[samples//2:])) < 1e-12
            assert max(abs(modes[n]) for n in range(2, 40, 2)) < 2e-12
        if params == (8, 1, 1, 1):
            assert abs(plus / period - 1 / 3) < 1e-14
            for n in (18, 24, 30):
                predicted = asymptotic(n, *params)
                assert abs(modes[n] - predicted) <= 0.003 * abs(predicted)
        if params == (1, 2, 1, 2):
            for n in (24, 30, 36):
                predicted = asymptotic(n, *params)
                assert abs(modes[n] - predicted) < 0.003 * abs(predicted)
    print('INVERSE_BETA_FOURIER_JUMP_IDENTITIES_OK')


if __name__ == '__main__':
    run()
