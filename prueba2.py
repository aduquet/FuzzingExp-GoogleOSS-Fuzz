import atheris

with atheris.instrument_imports():
  # from ruamel import yaml as ruamel_yaml
  import sys
  import warnings

# Suppress all warnings.
warnings.simplefilter("ignore")

# ryaml = ruamel_yaml.YAML(typ="safe", pure=True)
# ryaml.allow_duplicate_keys = True


@atheris.instrument_func
def TestOneInput(input_bytes):
  fdp = atheris.FuzzedDataProvider(input_bytes)
  data = fdp.ConsumeIntList(2,2)

  print(data)

  # try:
  #   iterator = ryaml.load_all(data)
  #   for _ in iterator:
  #     pass
  # except ruamel_yaml.error.YAMLError:
  #   return

  # except Exception:
  #   input_type = str(type(data))
  #   codepoints = [hex(ord(x)) for x in data]
  #   sys.stderr.write(
  #       "Input was {input_type}: {data}\nCodepoints: {codepoints}".format(
  #           input_type=input_type, data=data, codepoints=codepoints))
  #   raise


def main():
  atheris.Setup(sys.argv, TestOneInput)
  atheris.Fuzz()


if __name__ == "__main__":
  main()