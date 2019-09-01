# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_formatfile_session',
  :secret      => 'b595849ec0998702637ff20608041e3f498d2318ce903544ab1cd0da40d0b0b8b25fab324d037d90b7b7b363f07ebedac39901cf7223e64502c50c95256c46ab'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
