"""Define CharacterModel class."""
from typing import Callable, Dict, Tuple

import numpy as np

from text_recognizer.models.base import Model
from text_recognizer.datasets.emnist import EmnistDataset
from text_recognizer.networks.mlp import mlp


class CharacterModel(Model):
    def __init__(self,
                 dataset_cls: type = EmnistDataset,
                 network_fn: Callable = mlp,
                 dataset_args: Dict = None,
                 network_args: Dict = None):
        """Define the default dataset and network values for this model."""
        super().__init__(dataset_cls, network_fn, dataset_args, network_args)

    def predict_on_image(self, image: np.ndarray) -> Tuple[str, float]:
        if image.dtype == np.uint8:
            image = (image / 255).astype(np.float32)
        # NOTE: integer to character mapping dictionary is self.data.mapping[integer]
        # Your code below (Lab 1)

        # Your code above (Lab 1)
        return predicted_character, confidence_of_prediction
