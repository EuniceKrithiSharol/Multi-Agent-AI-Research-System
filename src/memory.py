class AgentMemory:


    def __init__(

        self
    ):

        self.history = []


    def add(

        self,

        agent,

        output
    ):

        self.history.append({

            "Agent": agent,

            "Output": output
        })


    def get_history(

        self
    ):

        return self.history


    def clear(

        self
    ):

        self.history = []
