"""dataSet dataset."""
import tensorflow_datasets as tfds
import csv
import os
from PIL import Image
import glob
# TODO(dataSet): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.
It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""
# TODO(dataSet): BibTeX citation
_CITATION = """Using Terry's data set currently
"""
class Dataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for dataSet dataset."""
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(dataSet): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(416, 416, 3)),
            'label': tfds.features.ClassLabel(names=['Grapes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )
  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(dataSet): Downloads the data and defines the splits
    
    # TODO(dataSet): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(
            path='/content/drive/Shareddrives/EEC193ATrackC/data/image_dir_train',
            label_path='/content/drive/Shareddrives/EEC193ATrackC/data/Annotations/Test1.csv',
        ),
        'test': self._generate_examples(
            path='/content/drive/Shareddrives/EEC193ATrackC/data/image_dir_test',
            label_path='/content/drive/Shareddrives/EEC193ATrackC/data/Annotations/Traine1.csv',
        ),
    }
  def _generate_examples(self, path, label_path):
    # Read the input data out of the source files
   
    images = glob.glob(os.path.join(path, "*.jpg"))
    for path in images:
      with open(path, 'r') as file:
        #img = path.open(file)
        # Yields (key, example)
        yield path, {
          'image': path,
          'label': 'Grapes',
      }
    with open(label_path, "r") as f:
      for row in csv.DictReader(f):
        image_id = row['image_id']
        # And yield (key, feature_dict)
        yield images_path, {
          'image': images_path / f'{image_id}.jpeg',
      } 