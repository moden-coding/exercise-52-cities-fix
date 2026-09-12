#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd

from src.cities import cities


class TestCities(unittest.TestCase):

    def test_first(self):
        df = cities()
        cols = df.columns
        ind = df.index
        self.assertEqual(cols[0], "Population", msg="Incorrect first column name!")
        self.assertEqual(cols[1], "Total area", msg="Incorrect second column name!")

        np.testing.assert_array_equal(ind, ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"],
                                      err_msg="Index was incorrect!")

        self.assertEqual(df.iloc[0, 0], 643272, msg="Incorrect content in df.iloc[0,0]!")
        self.assertEqual(df.iloc[1, 1], 528.03, msg="Incorrect content in df.iloc[1,1]!")
        self.assertEqual(df.iloc[2, 0], 231853, msg="Incorrect content in df.iloc[2,0]!")
        self.assertEqual(df.iloc[3, 1], 240.35, msg="Incorrect content in df.iloc[3,1]!")

    def test_returns_a_dataframe(self):
        df = cities()
        self.assertIsInstance(
            df,
            pd.DataFrame,
            msg="cities() must return a pandas DataFrame. Got %r." % (type(df),),
        )

    def test_shape(self):
        df = cities()
        self.assertEqual(
            df.shape,
            (5, 2),
            msg="cities() should return a DataFrame with 5 rows (one per city) "
            "and 2 columns (Population, Total area). Got shape %r." % (df.shape,),
        )


if __name__ == '__main__':
    unittest.main()
