# Tetris

Tetris on klassinen peli, jossa pinotaan eri muotoisia palikoita pelikentälle, tavoitteena saada virheettömiä rivejä aikaiseksi. Peli on vielä vaiheessa.

##

- [Release](https://github.com/emeraldgcube/ot-harjoitustyo/releases/tag/viikko6)
## Python-versio

Sovellus on testattu Python-versiolla 3.8.

## Käyttö 

1. Asenna riippuvuudet ajamalla komentoriviltä `poetry install`
2. Käynnistä peli komennolla `poetry run invoke start`

## Testit

1. Aja komento `poetry run pytest` src-kansiossa

## Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

## Pylint

.pylintrc-tiedoston määräämät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```


## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/maarittelydokumentti_tetris.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
