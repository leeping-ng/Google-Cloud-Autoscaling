"""
Node template for creating custom nodes.
"""
import datetime
from typing import Any, Dict

import cv2
from peekingduck.pipeline.nodes.abstract_node import AbstractNode


class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.

    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """

    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does ___.

        Args:
            inputs (dict): Dictionary with keys "__", "__".

        Returns:
            outputs (dict): Dictionary with keys "__".
        """

        current_time = datetime.datetime.now()
        # output as '240621-15-09-13.xxx'
        time_str = current_time.strftime("%d%m%y-%H-%M-%S.%f")

        cv2.imwrite(f"{self.output_dir}/result_{time_str}.jpeg", inputs["img"])
        return {}
