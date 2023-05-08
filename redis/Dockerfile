FROM redis:6.0-alpine

# Copy the Redis configuration file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose the Redis port
EXPOSE 6379

# Start Redis with the specified configuration file
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
