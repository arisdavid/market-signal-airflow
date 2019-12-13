

def test_download_lse_universe(get_lse_data):
   """
    Test Download LSE Universe is Non Empty
   """

   assert len(get_lse_data) > 0