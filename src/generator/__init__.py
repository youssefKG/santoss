from .dataschema import FunctionDefinition, Prompt


class Generator:
    def __init__(self,
                 prompts: list[Prompt],
                 functions_definition: list[FunctionDefinition]) -> None:
        self.prompts: list[Prompt] = prompts
        self.functions_definition: list[FunctionDefinition] = functions_definition

    def run(self) -> None:
        for prompt in self.prompts:
            fun_def: FunctionDefinition = 





__all__ = ["Generator", "FunctionDefinition", "Prompt"]
