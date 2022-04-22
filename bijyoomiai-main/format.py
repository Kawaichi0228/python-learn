class Format:
    @staticmethod
    def highlight(msg) -> str:
        list_ = []
        list_.append("---------------------------------------------------")
        list_.append(msg)
        list_.append("---------------------------------------------------")
        join_text = "\n".join(list_)
        return join_text
        
    @staticmethod    
    def gume(msg) -> str:
        list_ = []
        list_.append("<<<")
        list_.append(msg)
        list_.append(">>>")
        join_text = " ".join(list_)
        return join_text
        
    @staticmethod    
    def normal(msg) -> str:
        return msg
