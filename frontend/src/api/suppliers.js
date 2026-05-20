import client from './client';

export const getSuppliers = (shopId) =>
  client
    .get(`/suppliers?shop_id=${shopId}`)
    .then((r) => r.data);

export const createSupplier = (shopId, data) =>
  client
    .post(`/suppliers?shop_id=${shopId}`, data)
    .then((r) => r.data);

export const updateSupplier = (id, data) =>
  client
    .put(`/suppliers/${id}`, data)
    .then((r) => r.data);

export const deleteSupplier = (id) =>
  client
    .delete(`/suppliers/${id}`)
    .then((r) => r.data);
