import json
import os
import sys
import time
import keyboard


import pygame as pg
pg.init()
pg.font.init()
Fonte = pg.font.SysFont("calibri",20)


class Arch:
    def load(path):
        with open(path) as fp:
            return json.load(fp)
    def save(txt,path):
        with open(path,"w") as fp:
            json.dump(txt,fp)

class Prime():
    def __init__(self):

        self.Json = Arch.load("Primes.json")


        self.TryNumber = self.Json[-1]
        self.NIntD = 0

    def Is(self, num):

        if num == 0 or num == 1:
            return False

        for iter in range(2, num):
            if num % iter == 0:
                return False
        else:
            return True

    def Gen(self):
        canvas = pg.display.set_mode((300, 300))
        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    print(self.NIntD)
                    sys.exit()


            self.TryNumber += 1

            if self.Is(self.TryNumber):
                yield self.TryNumber

                self.NIntD += 1




                FonteNPrime = Fonte.render(str(prime.TryNumber), True, [255] * 3)
                PosNPrime = (canvas.get_width() - FonteNPrime.get_width())//2,(canvas.get_height() - FonteNPrime.get_height())//2
                canvas.blit(FonteNPrime,PosNPrime)

                pg.display.update()

                canvas = pg.display.set_mode((FonteNPrime.get_width() + 150,Fonte.get_height() + 150))





    def Mine(self):
        for i in self.Gen():
            self.Json.append(self.TryNumber)
            Arch.save(self.Json,"Primes.json")



prime = Prime()
prime.Mine()
