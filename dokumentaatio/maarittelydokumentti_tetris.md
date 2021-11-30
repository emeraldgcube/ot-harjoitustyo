# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on tetris-tyyppinen peli, jota pelataan tietokoneen näppäimistöllä.

## Käyttöliittymäluonnos

Peli sisältää aloitusvalikon, josta voidaan aloittaa peli, mahdollisesti valitsemalla kahdesta moodista, sekä josta voidaan tarkastella hiscoreja.

### Pelin aikana

Pelin aikana nähdään tetris-kenttä, ja vasemmalla sivulla mahdollinen holdattu palikka, ja oikealla seuraava palikka. 

![IMG_1347](https://user-images.githubusercontent.com/78031592/142070744-e95d8630-cb1a-4ad9-8141-0ef4a0390ae5.JPG)

Tausta on kaunis (optional). Kentän koko noin 20 (korkeus) x 10 (leveys).


### Pelin jälkeen

Pelin jälkeen nähdään tekstikenttä ja "insert name", jonka jälkeen nähdään sijoittuminen hiscore-listaan ja ok-painike, joka siirtää takaisin menuun.

## Perusversion tarjoama toiminnallisuus

- Pelissä on pelikenttä ✔
- Palikkoja on 7 erilaista ✔
- Palikkoja voi kääntää ✔
- Palikat putoaa ✔
- Palikoita voi siirtää ✔
- Seuraavan palikan näkee ✔
- Palikat ei mene rajojen yli
- Palikat ei mene toistensa päälle
- Täysi palikkarivi katoaa
- Palikan voi holdata
- Pelaaja näkee pisteensä pelatessa ja pelin jälkeen
- Pelaaja voi tallettaa pisteensä hiscoreen

### Mitä tarvitsee päättää jossain kohtaa

-Miten anteeksiantavaa on palikan pyöritys ja liikutus korkealla tasolla

## Ajan salliessa


-Kaksinpeli: peliä pelataan kahdella kentälle, kaksi pelaajaa samanaikaisesti pelaten, ja toisen pelaajan clearaamat rivit ilmestyvät toisen pelaajan tetris-kentän pohjalle.

-Niin ja ne kaksi moodia, eli tyyliin marathon eli kauanko jaksat painaa ja sitten nopeutuva
