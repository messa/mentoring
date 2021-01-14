Had po síti
===========

Základy programování se sítí
----------------------------

Materiály:

- https://docs.python.org/3/howto/sockets.html
- https://docs.python.org/3/library/socket.html – viz zejména [Example](https://docs.python.org/3/library/socket.html#example)
- Bonus: https://realpython.com/python-sockets/

Zkus si v Pythonu vytvořit server a klient a zkus si komunikaci mezi nimi.

Materiál k řetězcům, byte řetězcům a kódování: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/


Síťové programování v Asyncio
-----------------------------

Materiály:

- https://naucse.python.cz/course/mi-pyt/intro/async/
- https://docs.python.org/3/library/asyncio-stream.html

Zkus kód v předchozí části předělat do asyncio.

Důvodem k použití asyncio je možnost nějak relativně snadno řešit komunikaci s více klienty (anebo servery) najednou, což v serveru pro multiplayer hru bude potřeba.


Had
---

V základu jde o úlohu z Pyladies kurzu: https://naucse.python.cz/2020/pyladies-praha-podzim2020/projects/snake/

Pomocné materiály:

- https://pyvec.github.io/cheatsheets/pyglet/pyglet-basics-cs.pdf

Doporučuji vyzkoušet si nejdříve úpravu hry tak, aby v ní mohlo být více hadů.


Had po síti
-----------

Bude se skládat ze dvou částí:

- server udržuje stav hry, rozhoduje "co se děje"
- klient pravidelně dostává stav hry ze serveru, zobrazuje ho, a přeposílá příkazy (tj. směr hada) na server

