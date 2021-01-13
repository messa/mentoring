Had po síti
===========

Základy programování se sítí
----------------------------

Materiály:

- https://docs.python.org/3/howto/sockets.html
- https://docs.python.org/3/library/socket.html
- Bonus: https://realpython.com/python-sockets/

Zkus si v Pythonu vytvořit server a klient a zkus si komunikaci mezi nimi.


Síťové programování v Asyncio
-----------------------------

Materiály:

- https://docs.python.org/3/library/asyncio-stream.html

Zkus kód v předchozí části předělat do asyncio.

Důvodem k použití asyncio je možnost nějak relativně snadno řešit komunikaci s více klienty (anebo servery) najednou, což v serveru pro multiplayer hru bude potřeba.


Had po síti
-----------

Bude se skládat ze dvou částí:

- server udržuje stav hry, rozhoduje "co se děje"
- klient pravidelně dostává stav hry ze serveru, zobrazuje ho, a přeposílá příkazy (tj. směr hada) na server

