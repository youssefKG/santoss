from .error import CallError
from .generator import Generator, FunctionDefinition, Prompt


import json
import argparse

class Json():
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
                    prog='ProgramName')
        self.__add_args()

    def __add_args(self) -> None:
        self.parser.add_argument(
                "--functions_definition"
                )
        self.parser.add_argument(
                "--input"
                )
        self.parser.add_argument(
                "--ouput"
                )

    def get_functions_definition(self) -> list[FunctionDefinition]:
        with open("data/input/functions_definition.json", 'r') as data:
            functions_definition: list[dict[str, str]] = json.load(data)
        return [FunctionDefinition(**fundefinition) for fundefinition in functions_definition]

    def get_prompts(self) -> list[Prompt]:
        with open("data/input/function_calling_tests.json", 'r') as data:
            prompts:  dict[str, str] = json.load(data)
        return [Prompt(**prompt) for prompt in prompts]


def main() -> None:
    data = Json()
    trie: PrifixTrie = ()
    Generator(
            prompts=data.get_prompts(),
            functions_definition=data.get_functions_definition()
            ).run()

if __name__ == "__main__":
    try:
        main()
    except CallError as e:
        e.print()

