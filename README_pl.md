# Coax Calculator

Kalkulator strat w kablach koncentrycznych.

Pozwala obliczyć stratę mocy w sygnale w. cz. dla różnych kabli koncentrycznych, w zależności od częstotliwości, długości i mocy wejściowej.

## Jak to działa

Najważniejszyme elementem jest plik [cables](cables.yaml). Zawiera on dane o tłumieniu różnych typów kabli, podawane przez producenta dla różnych częstoliwości. Dane są pozyskane z oficjalnych not katalogowych:

```yaml
h155-belden:
  name: H155 (Belden)
  manufacturer: Belden
  type: H155
  attenuation: { 5: 2.5, 50: 6.9, 100: 9.1, 230: 13.4, 400: 18.0, 800: 26.1, 862: 27.3, 1000: 29.6, 1350: 34.9, 1750: 40.3, 2150: 46.0, 2400: 49.1, 3000: 56.3, 4200: 69.1, 5800: 75.1, 5400: 80.8, 6000: 86.5 }
  data_source: https://www.tme.eu/Document/18ee3e29381bee0e348180bedff1050b/H155BK_EN.PDF
  additional_info:
    ext_diameter_mm: 5.4
    velocity_factor: 0.8
    impedance: 50
```

Ponieważ wartości tłumienia są podawane dla konkretnych częstotliwości, zastosowano prostą [interpolację liniowa](https://pl.wikipedia.org/wiki/Interpolacja_liniowa), aby uzyskać przybliżone tłumienie dla dowolnej interesującej nas częstotliwości.

## Brakuje kabla X

Jeśli Twojego ulubionego kabla nie ma na liście, to zmodyfikuj plik `cables.yaml`, uzupełniając wszystkie pola jak w przykładzie powyżej i otwórz pull request.