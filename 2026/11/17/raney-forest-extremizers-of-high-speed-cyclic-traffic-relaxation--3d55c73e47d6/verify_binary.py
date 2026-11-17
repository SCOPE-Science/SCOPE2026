"""Direct physical car-position simulation, without using gap-state dynamics."""
from itertools import combinations
from math import comb

def update(positions, length, speed):
    size = len(positions)
    result = []
    for i, car in enumerate(positions):
        next_car = positions[(i+1) % size] + (length if i == size-1 else 0)
        move = min(next_car-car-1, speed)
        result.append((car+move) % length)
    return tuple(sorted(result))

def free(positions, length, speed):
    return all((positions[(i+1) % len(positions)] +
                (length if i == len(positions)-1 else 0) - car - 1) >= speed
               for i,car in enumerate(positions))

def run():
    for speed,cars,surplus in ((1,3,0),(1,5,2),(2,3,0),(2,4,0),
                               (2,4,3),(3,3,1),(3,4,0),(4,3,0)):
        length = (speed+1)*cars+surplus
        count = 0
        last = 0
        for pos in combinations(range(length),cars):
            current=pos
            t=0
            while not free(current,length,speed):
                current=update(current,length,speed)
                t+=1
                assert t <= cars-1
            count+=1
            last+=t==cars-1
        expected=length*comb((speed+1)*cars-2,cars-1)//cars
        assert count==comb(length,cars)
        assert last==expected, (speed,cars,surplus,last,expected)
        print('speed=%d cars=%d sites=%d extremal=%d total=%d PASS' %
              (speed,cars,length,last,count))

if __name__=='__main__':
    run()
