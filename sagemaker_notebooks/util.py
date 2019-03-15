def get_image(name, sess):
    account = sess.boto_session.client('sts').get_caller_identity()['Account']
    region = sess.boto_session.region_name
    return f'{account}.dkr.ecr.{region}.amazonaws.com/{name}:latest'


def upload_data(data_directory, s3_prefix, sess):
    """Upload `data_directory` to s3.
    
    e.g. upload_data('data', s3_prefix='bucket')
    """
    return sess.upload_data(data_directory, key_prefix=s3_prefix)
