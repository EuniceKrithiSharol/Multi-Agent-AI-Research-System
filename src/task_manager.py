class TaskManager:


    def create_task(

        self,

        query
    ):

        return {

            "task": query,

            "status": "Pending"
        }


    def update_status(

        self,

        task,

        status
    ):

        task[
            "status"
        ] = status


        return task
