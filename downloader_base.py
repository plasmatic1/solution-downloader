# American Born Chinese
from abc import ABC, abstractmethod


class SubmissionDownloader(ABC):
    @abstractmethod
    def __init__(self, handle_info, cfg):
        """
        :param handle_info: Information on the handle
        :param cfg: Other config keys
        """
        pass

    @abstractmethod
    def get_accepted_subs(self) -> list[tuple[str, str]]:
        """
        Returns a list of accepted submissions for a user
        :return: A list tuple[submission id, file name for problem]
        """
        pass

    @abstractmethod
    def get_source(self, sub_id: str) -> str:
        """
        Retrieves the source code for a submission ID
        :param sub_id: The submission id of the source
        :return: The source code for a submission ID
        """
        pass

    @abstractmethod
    def file_ext(self, lang: str) -> str:
        """
        Retrieves the file extension to be used for that language
        :param lang: The language
        :return: The file extension to be used for that language
        """
        pass
