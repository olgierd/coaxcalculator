# Coax Calculator
Open source coaxial cable loss calculator.

Calculates total loss for various feedlines, based on frequency, length and input power.

## How does it work?

The most important part of the calculator is [cables](cables.yaml) file. It contains attenuation data specified by cable manufacturer for various frequencies, extracted from the datasheet:

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

Since the attenuation is specified for a given frequency values, usually different for every manufacturer, a simple [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) is performed.

## How to contribute?

If your favourite cable is not on the list, please add it to `cables.yaml`, including all the fields as in the example above and open a pull request.